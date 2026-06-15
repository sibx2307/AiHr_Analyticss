import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import Attendance from "./pages/Attendance";
import Performance from "./pages/Performance";
import Anomalies from "./pages/Anomalies";
import Employees from "./pages/Employees";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import UploadData from "./pages/UploadData";

import ProtectedRoute
from "./components/ProtectedRoute";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>

              <Dashboard />

            </ProtectedRoute>
          }
        />
        <Route
          path="/employees"
          element={
            <ProtectedRoute>
              <Employees />
            </ProtectedRoute>
          }
        />
        <Route 
          path="/attendance"
          element={<Attendance />

          } 
        />
        <Route
          path="/performance"
          element={
            <Performance />
          }
        />
        <Route
          path="/anomalies"
          element={
            <Anomalies />
          }
        />
        <Route
          path="/upload"
          element={
              <ProtectedRoute>
                  <UploadData />
              </ProtectedRoute>
          }
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;