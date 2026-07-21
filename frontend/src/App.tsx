import PageHeader from "./components/PageHeader";
import UploadArea from "./components/UploadArea";
import SuggestedPrompts from "./components/SuggestedPrompts";
import ChatWindow from "./components/ChatWindow";
import PromptInput from "./components/PromptInput";

import { useChat } from "./hooks/useChat";

export default function App() {
    const {
        messages,
        prompt,
        setPrompt,
        send,
    } = useChat();

    return (
        <main className="mx-auto flex min-h-screen max-w-4xl flex-col px-6 py-8">
            <PageHeader />

            <div className="mt-8 space-y-6">
                <UploadArea />

                <SuggestedPrompts
                    onPromptClick={setPrompt}
                />

                <ChatWindow
                    messages={messages}
                />

                <PromptInput
                    prompt={prompt}
                    setPrompt={setPrompt}
                    onSend={send}
                />
            </div>
        </main>
    );
}