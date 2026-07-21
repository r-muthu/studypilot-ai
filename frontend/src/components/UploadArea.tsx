import type { ChangeEvent } from "react";
import { Upload } from "lucide-react";
import { useUpload } from "../hooks/useUpload";

export default function UploadArea() {
    const {
        selectedFile,
        uploading,
        uploaded,
        upload,
    } = useUpload();

    const handleFileChange = async (
        event: ChangeEvent<HTMLInputElement>
    ) => {
        const file = event.target.files?.[0];

        if (!file) return;

        await upload(file);
    };

    return (
        <div className="rounded-2xl border border-dashed border-gray-300 bg-white p-8 shadow-sm">
            <div className="flex flex-col items-center text-center">
                <Upload className="mb-4 h-10 w-10 text-blue-600" />

                <h2 className="text-xl font-semibold">
                    Upload a Document
                </h2>

                <p className="mt-2 text-sm text-gray-500">
                    Drag and drop a PDF here, or click below to select one.
                </p>

                <input
                    type="file"
                    accept=".pdf"
                    onChange={handleFileChange}
                    className="mt-6 block text-sm"
                />

                {uploading && (
                    <p className="mt-4 text-sm text-blue-600">
                        Uploading...
                    </p>
                )}

                {uploaded && selectedFile && (
                    <p className="mt-4 text-sm text-green-600">
                        ✓ {selectedFile.name} uploaded successfully.
                    </p>
                )}

                <p className="mt-3 text-xs text-gray-400">
                    Supported format: PDF
                </p>
            </div>
        </div>
    );
}