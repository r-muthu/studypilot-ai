import { SendHorizontal } from "lucide-react";

interface PromptInputProps {
    prompt: string;
    setPrompt: (value: string) => void;
    onSend: () => void;
}

export default function PromptInput({
    prompt,
    setPrompt,
    onSend,
}: PromptInputProps) {
    return (
        <div className="flex gap-3">
            <input
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                        onSend();
                    }
                }}
                type="text"
                placeholder="Ask anything about your document..."
                className="flex-1 rounded-xl border px-4 py-3 outline-none focus:border-blue-500"
            />

            <button
                onClick={onSend}
                className="rounded-xl bg-blue-600 px-5 text-white hover:bg-blue-700"
            >
                <SendHorizontal className="h-5 w-5" />
            </button>
        </div>
    );
}