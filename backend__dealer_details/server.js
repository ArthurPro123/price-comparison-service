const express = require("express");
const cors = require("cors");
const knex = require("knex")({
    client: "sqlite3",
    connection: {
        filename: "./dealers.db",
    },
    useNullAsDefault: true,
});

const app = express();

// Enable CORS only in development
if (process.env.RUNNING_MODE === "development") {
  app.use(cors({
    origin: "http://localhost:5001",
    methods: ["GET", "POST", "OPTIONS"],
    allowedHeaders: ["Content-Type", "Authorization"],
  }));
}

// Initialize the database and insert sample data
async function initDb() {
    try {
        console.log("Initializing database...");

        // Check if the table exists
        const hasDealers = await knex.schema.hasTable("dealers");
        console.log(`Table exists: ${hasDealers}`);

        if (!hasDealers) {
            console.log("Creating dealers table...");

            // Create the dealers table
            await knex.schema.createTable("dealers", (table) => {
                table.increments("id").primary();
                table.string("name").unique().notNullable();
                table.jsonb("products").notNullable();
            });

            console.log("Inserting sample data...");

            // Insert sample data
            await knex("dealers").insert([
                { name: "Binglee", products: JSON.stringify({ Headphones: "$30", Printer: "$75" }) },
                { name: "DXC Electronics", products: JSON.stringify({ Mouse: "$20", Printer: "$85", Headphones: "$20" }) },
                { name: "Bobay", products: JSON.stringify({ Headphones: "$20", Printer: "$80" }) },
                { name: "Tech City", products: JSON.stringify({ Mouse: "$20", Laptop: "$850" }) },
                { name: "Ez PC", products: JSON.stringify({ Laptop: "$1000" }) },
                { name: "GH Computers", products: JSON.stringify({ Laptop: "$1500", Printer: "$95" }) },
            ]);

            console.log("Sample data inserted successfully!");
        } else {
            console.log("Table already exists. Skipping data insertion.");
        }
    } catch (error) {
        console.error("Error initializing database:", error);
    }
}

// Initialize the database
initDb().then(() => {
    // Endpoint to get price for a specific dealer and product
    app.get("/price/:dealer/:product", async (req, res) => {
        try {
            const { dealer, product } = req.params;
            const row = await knex("dealers").where({ name: dealer }).first();

            if (!row) {
                return res.status(404).json({ message: "Dealer not found" });
            }

            const products = JSON.parse(row.products);
            if (products[product]) {
                res.json({ message: `${product} costs ${products[product]} at ${dealer}` });
            } else {
                res.json({ message: `${product} is not available with ${dealer}` });
            }
        } catch (error) {
            console.error("Error fetching price:", error);
            res.status(500).json({ error: "Internal server error" });
        }
    });

    // Endpoint to get all prices for a product
    app.get("/allprice/:product", async (req, res) => {
        try {
            const { product } = req.params;
            const rows = await knex("dealers").select("*");

            const prices = rows
                .filter((row) => {
                    const products = JSON.parse(row.products);
                    return products[product];
                })
                .map((row) => {
                    const products = JSON.parse(row.products);
                    return { key: row.name, value: products[product] };
                });

            if (prices.length > 0) {
                res.json({ prices });
            } else {
                res.json({ message: `No dealers found for ${product}` });
            }
        } catch (error) {
            console.error("Error fetching all prices:", error);
            res.status(500).json({ error: "Internal server error" });
        }
    });

    // Start the server
    const port = process.env.PORT || 8080;
    app.listen(port, () => {
        console.log(`Server running on port ${port}`);
    });
});
