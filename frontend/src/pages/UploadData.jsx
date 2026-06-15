import { useState } from "react";
import Layout from "../components/Layout";
import API from "../api/api";

function UploadData() {

    const [file, setFile] = useState(null);

    const uploadFile = async () => {

        const formData = new FormData();

        formData.append(
            "file",
            file
        );

        try {

            await API.post(
                "/upload/employees",
                formData,
                {
                    headers: {
                        "Content-Type":
                            "multipart/form-data"
                    }
                }
            );

            alert(
                "Upload successful"
            );

        } catch (error) {

            alert(
                "Upload failed"
            );
        }
    };

    return (

        <Layout>

            <h2>Upload Employee Data</h2>

            <input
                type="file"
                className="form-control"
                onChange={(e) =>
                    setFile(
                        e.target.files[0]
                    )
                }
            />

            <button
                className="btn btn-primary mt-3"
                onClick={uploadFile}
            >
                Upload CSV
            </button>

        </Layout>
    );
}

export default UploadData;