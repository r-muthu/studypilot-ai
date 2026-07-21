import { Bot, User } from "lucide-react";
import type { ChatMessage } from "../types/chat";

export default function MessageBubble({
    role,
    message,
}: ChatMessage) {
    const isUser = role === "user";

    return (
        <div
            className={`flex gap-3 ${
                isUser ? "justify-end" : "justify-start"
            }`}
        >
            {!isUser && (
                <div className="rounded-full bg-blue-100 p-2">
                    <Bot className="h-5 w-5 text-blue-600" />
                </div>
            )}

            <div
                className={`max-w-[75%] rounded-2xl px-4 py-3 text-sm ${
                    isUser
                        ? "bg-blue-600 text-white"
                        : "bg-gray-100 text-gray-900"
                }`}
            >
                {message}
            </div>

            {isUser && (
                <div className="rounded-full bg-gray-200 p-2">
                    <User className="h-5 w-5 text-gray-700" />
                </div>
            )}
        </div>
    );
}