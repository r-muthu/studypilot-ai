interface SuggestedPromptsProps {
    onPromptClick: (prompt: string) => void;
}

const prompts = [
    "Summarise this paper",
    "Explain the methodology",
    "Generate 10 quiz questions",
    "What are the key findings?",
];

export default function SuggestedPrompts({
    onPromptClick,
}: SuggestedPromptsProps) {
    return (
        <div>
            <h2 className="mb-3 text-sm font-semibold text-gray-600">
                Suggested Prompts
            </h2>

            <div className="flex flex-wrap gap-2">
                {prompts.map((prompt) => (
                    <button
                        key={prompt}
                        onClick={() => onPromptClick(prompt)}
                        className="rounded-full border px-4 py-2 text-sm hover:bg-gray-100"
                    >
                        {prompt}
                    </button>
                ))}
            </div>
        </div>
    );
}