import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import API from "../api/api";

import {
    PieChart,
    Pie,
    Cell,
    Tooltip
} from "recharts";

function Attendance() {

    const [stats, setStats] = useState({
        present: 0,
        absent: 0,
        avg_hours: 0
    });

    useEffect(() => {
        fetchStats();
    }, []);

    const fetchStats = async () => {

        const response =
            await API.get(
                "/attendance/stats"
            );

        setStats(
            response.data
        );
    };

    const data = [
        {
            name: "Present",
            value: stats.present
        },
        {
            name: "Absent",
            value: stats.absent
        }
    ];

    return (

        <Layout>

            <h2>Attendance Analytics</h2>

            <div className="row mt-4">

                <div className="col-md-4">

                    <div className="card p-3">

                        <h5>Present</h5>

                        <h2>
                            {stats.present}
                        </h2>

                    </div>

                </div>

                <div className="col-md-4">

                    <div className="card p-3">

                        <h5>Absent</h5>

                        <h2>
                            {stats.absent}
                        </h2>

                    </div>

                </div>

                <div className="col-md-4">

                    <div className="card p-3">

                        <h5>Avg Hours</h5>

                        <h2>
                            {stats.avg_hours}
                        </h2>

                    </div>

                </div>

            </div>

            <div className="mt-5">

                <PieChart
                    width={400}
                    height={300}
                >

                    <Pie
                        data={data}
                        dataKey="value"
                        outerRadius={100}
                        label
                    >

                        <Cell />
                        <Cell />

                    </Pie>

                    <Tooltip />

                </PieChart>

            </div>

        </Layout>
    );
}

export default Attendance;