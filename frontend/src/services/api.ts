import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
    },
});

// ---------- Types ----------

export interface ChatResponse {
    response: string;
    tool_used?: string;
    sources?: {
        page: number;
        text: string;
    }[];
}

export interface UploadResponse {
    filename: string;
    pages: number;
    chunks: number;
    message: string;
}

// ---------- Health ----------

export async function healthCheck() {
    const response = await api.get("/health");
    return response.data;
}

// ---------- Upload PDF ----------

export async function uploadPDF(file: File): Promise<UploadResponse> {
    const formData = new FormData();
    formData.append("file", file);

    const response = await api.post("/upload", formData, {
        headers: {
            "Content-Type": "multipart/form-data",
        },
    });

    return response.data;
}

// ---------- Chat ----------

export async function sendMessage(
    message: string
): Promise<ChatResponse> {
    const response = await api.post("/chat", {
        message,
    });

    return response.data;
}

export default api;