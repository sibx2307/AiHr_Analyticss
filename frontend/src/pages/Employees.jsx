import { useEffect, useState } from "react";
import API from "../api/api";
import Layout from "../components/Layout";

function Employees() {

    const [employees, setEmployees] = useState([]);

    const [name, setName] = useState("");
    const [department, setDepartment] = useState("");
    const [salary, setSalary] = useState("");

    useEffect(() => {
        fetchEmployees();
    }, []);

    const fetchEmployees = async () => {

        const response =
            await API.get("/employees");

        setEmployees(response.data);
    };

    const addEmployee = async (e) => {

        e.preventDefault();

        await API.post("/employees", {
            name,
            department,
            salary
        });

        setName("");
        setDepartment("");
        setSalary("");

        fetchEmployees();
    };
const deleteEmployee = async (id) => {

    if (!window.confirm("Delete this employee?")) {
        return;
    }

    await API.delete(`/employees/${id}`);

    fetchEmployees();
};
    return (
        <Layout>
            <div className="container mt-4">

                <h2>Employee Management</h2>

                <div className="card p-3 mb-4">

                    <h4>Add Employee</h4>

                    <form onSubmit={addEmployee}>

                        <input
                            className="form-control mb-2"
                            placeholder="Employee Name"
                            value={name}
                            onChange={(e) =>
                                setName(e.target.value)
                            }
                        />

                        <input
                            className="form-control mb-2"
                            placeholder="Department"
                            value={department}
                            onChange={(e) =>
                                setDepartment(e.target.value)
                            }
                        />

                        <input
                            className="form-control mb-2"
                            placeholder="Salary"
                            value={salary}
                            onChange={(e) =>
                                setSalary(e.target.value)
                            }
                        />

                        <button
                            className="btn btn-success"
                        >
                            Add Employee
                        </button>

                    </form>

                </div>

                <table className="table table-striped">

                    <thead>

                        <tr>

                            <th>ID</th>
                            <th>Name</th>
                            <th>Department</th>
                            <th>Salary</th>
                            <th>Actions</th>

                        </tr>

                    </thead>

                    <tbody>

                        {
                            employees.map((emp) => (

                                <tr key={emp.id}>

                                    <td>{emp.id}</td>
                                    <td>{emp.name}</td>
                                    <td>{emp.department}</td>
                                    <td>{emp.salary}</td>

                                    <td>

                                        <button
                                            className="btn btn-danger btn-sm"
                                            onClick={() =>
                                                deleteEmployee(emp.id)
                                            }
                                        >
                                            Delete
                                        </button>

                                    </td>

                                </tr>
                            ))
                        }

                    </tbody>

                </table>

            </div>
        </Layout> 
    );
}

export default Employees;