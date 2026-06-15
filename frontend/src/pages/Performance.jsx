import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import API from "../api/api";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

function Performance() {

  const [stats, setStats] = useState({
    avg_rating: 0,
    total_reviews: 0,
    projects: []
  });

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {

    const response =
      await API.get(
        "/performance/stats"
      );

    setStats(
      response.data
    );
  };

  return (

    <Layout>

      <h2>Performance Analytics</h2>

      <div className="row mt-4">

        <div className="col-md-6">

          <div className="card p-3">

            <h5>Average Rating</h5>

            <h2>
              {stats.avg_rating}
            </h2>

          </div>

        </div>

        <div className="col-md-6">

          <div className="card p-3">

            <h5>Total Reviews</h5>

            <h2>
              {stats.total_reviews}
            </h2>

          </div>

        </div>

      </div>

      <div className="mt-5">

        <BarChart
          width={700}
          height={350}
          data={stats.projects}
        >

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="project" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="count" />

        </BarChart>

      </div>

    </Layout>
  );
}

export default Performance;