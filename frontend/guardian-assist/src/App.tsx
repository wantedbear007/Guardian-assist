import React, { useState } from "react";
import logo from "./assets/logo.png";
import aiAvatar from "./assets/ai.jpg";
import humanAvatar from "./assets/human.jpg";

import axios from "axios";

interface Props {
  message: string;
  image: number;
}

// const url: string = "http://127.0.0.1:8000/v1/";
const url: string = (import.meta.env.VITE_BACKEND_URL);


// Chat card
const ChatCard: React.FC<Props> = ({ message, image }) => {
  return (
    <div className="flex items-center mb-5 px-8">
      <img
        src={image == 1 ? aiAvatar : humanAvatar}
        alt="Profile"
        className="w-12 h-12 rounded-full mr-4"
      />
      <div className="bg-gray-100 p-3 px-10 rounded-lg">
        <p className="text-sm">{message}</p>
      </div>
    </div>
  );
};

export default function App() {
  const [inputValue, setInputValue] = useState("");
  const [fileName, setFileName] = useState<string>("");
  const [fileURL, setFileURL] = useState<string>();
  const [uploading, setUploading] = useState<boolean>(false);
  const [chat, addChat] = useState<{ message: string; image: number }[]>([]);
  const [chatLoading, setChatLoading] = useState<boolean>(false);

  const handleClick = async () => {
    const fileInput = document.getElementById("fileInput");
    if (fileInput) fileInput.click();
  };

  const uploadFile = async (file: File) => {
    setUploading(true);
    const data = new FormData();
    data.append("file", file);

    try {
      const response = await axios.post(url + "upload", data, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      if (response.status != 200) {
        alert("Something went wrong. Try again.");
        return;
      }
      const fileLink: string = response.data["file_id"];
      setFileURL(fileLink);
      setUploading(false);
    } catch (err) {
      alert("Something went wrong while uploading file.");
      setUploading(false);
    }
  };

  const handleFileChange = async (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    if (event.target.files && event.target.files.length > 0) {
      const file = event.target.files[0];

      if (file.type != "application/pdf") {
        console.log("error hai");
        alert("File type not allowed, Upload pdf.");
        return;
      }

      // setSelectedFile(file);
      setFileName(file.name);
      await uploadFile(file);
    }
  };

  // send messages
  async function sendMessage(query: string) {
    if (inputValue.trim() !== "") {
      addChat((prevChat) => [
        ...prevChat,
        {
          message: inputValue,
          image: 2,
        },
      ]);

      setInputValue("");
      setChatLoading(true);
      const data = JSON.stringify({
        doc_url: fileURL,
        query: query,
      });

      try {
        const response = await axios.post(url + "chat/", data, {
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (response.status !== 200) {
          alert("Something went wrong. Try again.");
          return;
        }

        addChat((prevChat) => [
          ...prevChat,
          {
            message: response.data.response,
            image: 1,
          },
        ]);
      } catch (err) {
        alert("Something went wrong. Try again.");
        console.error(err);
      } finally {
        setChatLoading(false);
      }
    } else {
      alert("Please enter a message.");
    }
  }

  const handleSubmit = async () => {
    await sendMessage(inputValue);
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };

  return (
    <main className="flex flex-col justify-between min-h-screen">
      {/* top navigation */}
      <div className="flex flex-row items-center justify-between bg-gray-100 px-5 py-10 shadow-lg">
        <img src={logo} height={120} width={120} alt="company logo" />
        <div style={{ display: "flex", alignItems: "center" }}>
          <h1 className="font-medium">{fileName}</h1>

          <div className="mx-5">
            <input
              id="fileInput"
              type="file"
              style={{ display: "none" }}
              onChange={handleFileChange}
            />
            <button
              className="flex items-center px-10 py-3 bg-green-500 text-white rounded-lg hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
              onClick={handleClick}
            >
              <span className="mr-2 font-semibold">+</span>
              <span className="font-semibold">
                {!uploading ? "Upload PDF" : "Uploading"}
              </span>
            </button>
          </div>
        </div>
      </div>
      {/* chat section */}
      <div className="min-h-fit max-w-full">
        {!fileURL && (
          <div>
            <h1 className="text-5xl text-center">
              Ask, Learn, and Explore Your
              <span className="text-green-400"> PDFs</span>
            </h1>
          </div>
        )}

        <div className="">
          {chat.map((chatItem, index) => (
            <ChatCard
              key={index}
              message={chatItem.message}
              image={chatItem.image}
            />
          ))}

          {chatLoading && (
            <h1 className="px-10">Your answer is on the way...</h1>
          )}
        </div>
      </div>

      {/* footer */}
      <div className="flex justify-center py-10 bg-gray-100 ">
        <input
          value={inputValue}
          onChange={handleChange}
          placeholder={
            fileURL
              ? "Send a message..."
              : "Upload your file and Start Asking !"
          }
          className="transition ease-in-out delay-150 rounded-xl px-8 py-2 mx-20 focus:ring-2 focus:ring-green-500"
          style={{ width: "90%" }}
          disabled={fileURL ? false : true}
        />

        {fileURL && (
          <button
            className="transition ease-in-out delay-50 hover:bg-gray-200 relative bottom-2 right-12 mt-3 mr-3 text-gray-800 rounded-xl px-4 py-2"
            onClick={handleSubmit}
          >
            Send ➤
          </button>
        )}
      </div>
    </main>
  );
}
