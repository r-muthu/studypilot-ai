import MessageBubble from "./MessageBubble";
import type { ChatMessage } from "../types/chat";

interface ChatWindowProps {
    messages: ChatMessage[];
}

export default function ChatWindow({
    messages,
}: ChatWindowProps) {
    return (
        <div className="rounded-2xl border bg-white shadow-sm">
            <div className="border-b px-6 py-4">
                <h2 className="text-lg font-semibold">
                    Conversation
                </h2>
            </div>

            <div className="space-y-4 p-6">
                {messages.map((msg, index) => (
                    <MessageBubble
                        key={index}
                        role={msg.role}
                        message={msg.message}
                    />
                ))}
            </div>
        </div>
    );
}