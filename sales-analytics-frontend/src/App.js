import React, { useState, useEffect } from "react";

function App() {
    const [salesData, setSalesData] = useState([]);

    useEffect(() => {
        fetch("/api/sales")
            .then(response => response.json())
            .then(data => setSalesData(data));
    }, []);

    return (
        <div>
            <h1>Sales Analytics Dashboard</h1>
            <table>
                <thead>
                    <tr>
                        <th>Region</th>
                        <th>Product</th>
                        <th>Sales</th>
                        <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    {salesData.map((item, index) => (
                        <tr key={index}>
                            <td>{item.region}</td>
                            <td>{item.product}</td>
                            <td>{item.sales}</td>
                            <td>{item.timestamp}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default App;

