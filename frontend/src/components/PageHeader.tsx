import { BookOpenText } from "lucide-react";

export default function PageHeader() {
    return (
        <header className="text-center">
            <div className="mb-4 flex justify-center">
                <div className="rounded-full bg-blue-100 p-3">
                    <BookOpenText className="h-8 w-8 text-blue-600" />
                </div>
            </div>

            <h1 className="text-4xl font-bold tracking-tight">
                StudyPilot AI
            </h1>

            <p className="mx-auto mt-3 max-w-2xl text-gray-600">
                Upload academic papers or lecture notes and let an
                AI agent help you understand, analyse and study them.
            </p>
        </header>
    );
}