export interface UploadState {
    selectedFile: File | null;
    uploading: boolean;
    uploaded: boolean;
    filename: string;
}