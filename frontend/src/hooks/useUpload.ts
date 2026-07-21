import { useState } from "react";
import { uploadPDF } from "../services/api";

export function useUpload() {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [uploading, setUploading] = useState(false);
    const [uploaded, setUploaded] = useState(false);

    async function upload(file: File) {
        setSelectedFile(file);
        setUploading(true);

        try {
            await uploadPDF(file);
            setUploaded(true);
        } finally {
            setUploading(false);
        }
    }

    return {
        selectedFile,
        uploading,
        uploaded,
        upload,
    };
}