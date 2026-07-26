import { useState } from "react";
import { sendMessage } from "../services/api";
import type { ChatMessage } from "../types/chat";

export function useChat() {
    const [conversationId] = useState(() => crypto.randomUUID());
    
    const [messages, setMessages] = useState<ChatMessage[]>([
        {
            role: "assistant",
            message:
                "👋 Welcome to StudyPilot! Upload a PDF and ask me anything.",
        },
    ]);

    const [prompt, setPrompt] = useState("");

    async function send() {
        if (!prompt.trim()) return;

        const userPrompt = prompt;

        setMessages((prev) => [
            ...prev,
            {
                role: "user",
                message: userPrompt,
            },
        ]);

        setPrompt("");

        try {
            const response = await sendMessage(conversationId, userPrompt);

            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    message: response.response,
                },
            ]);
        } catch {
            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    message: "Unable to contact backend.",
                },
            ]);
        }
    }

    return {
        messages,
        prompt,
        setPrompt,
        send,
    };
}