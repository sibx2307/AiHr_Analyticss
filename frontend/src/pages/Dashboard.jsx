function Dashboard() {

    return (

        <div className="container mt-5">

            <h1>
                AI HR Analytics Dashboard
            </h1>

            <hr />

            <div className="row">

                <div className="col-md-3">

                    <div className="card p-3">

                        <h5>
                            Employees
                        </h5>

                        <h2>
                            150
                        </h2>

                    </div>

                </div>

                <div className="col-md-3">

                    <div className="card p-3">

                        <h5>
                            Attendance
                        </h5>

                        <h2>
                            94%
                        </h2>

                    </div>

                </div>

                <div className="col-md-3">

                    <div className="card p-3">

                        <h5>
                            Performance
                        </h5>

                        <h2>
                            4.2
                        </h2>

                    </div>

                </div>

                <div className="col-md-3">

                    <div className="card p-3">

                        <h5>
                            Anomalies
                        </h5>

                        <h2>
                            7
                        </h2>

                    </div>

                </div>

            </div>

        </div>

    );
}

export default Dashboard;