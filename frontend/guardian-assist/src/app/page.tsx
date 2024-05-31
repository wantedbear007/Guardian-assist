"use client"

import { useState } from "react";
import Image from "next/image";
import logo from "../../public/logo.png";

interface Props {
  sender: string;
  message: string;
  image: string;
}

  // chat card
const ChatCard: React.FC<Props> = ({ sender, message, image }) => {
  return (
    <div className="flex items-center mb-5 px-8">
      <img
        src={image}
        alt="Profile"
        className="w-12 h-12 rounded-full mr-4"
      />
      <div className="bg-gray-100 p-3 px-10 rounded-lg">
        {/* <p className="text-sm font-medium">{sender}</p> */}
        <p className="text-sm">{message}</p>
      </div>
    </div>
  );
};

export default function Home() {

  const [inputValue, setInputValue] = useState("");

  function handleClick() {
    // Handle click logic here
  }

  function handleChange(event: any) {
    setInputValue(event.target.value);
  }

  return (
    <main className="flex flex-col justify-between min-h-screen">
      {/* top navigation */}
      <div className="flex flex-row items-center justify-between bg-gray-100 px-5 py-10 shadow-lg">
        <Image src={logo} height={120} width={120} alt="company logo" />
        <div>
          {/* add uploaded file name */}
          <button
            className="flex items-center px-10 py-3 bg-green-500 text-white rounded-lg hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
            onClick={handleClick}
          >
            <span className="mr-2 font-semibold">+</span>
            <span className="font-semibold">Upload PDF</span>
          </button>
        </div>
      </div>
      {/* chat section */}
      <div className="min-h-fit max-w-full">
        {/* Chat messages go here */}
        <ChatCard image="https://as1.ftcdn.net/v2/jpg/03/46/83/96/1000_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg" message="Hello from Bhanu" sender="Someone" />
        <ChatCard image="https://as1.ftcdn.net/v2/jpg/03/46/83/96/1000_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg" message="Hello from Bhanu" sender="Someone" />
        <ChatCard image="https://as1.ftcdn.net/v2/jpg/03/46/83/96/1000_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg" message="Hello from Bhanu" sender="Someone" />
        <ChatCard image="https://as1.ftcdn.net/v2/jpg/03/46/83/96/1000_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg" message="Hello from Bhanu" sender="Someone" />
        <ChatCard image="https://as1.ftcdn.net/v2/jpg/03/46/83/96/1000_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg" message="Hello from Bhanu" sender="Someone" />
        <ChatCard image="https://as1.ftcdn.net/v2/jpg/03/46/83/96/1000_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg" message="Hello from Bhanu" sender="Someone" />


      </div>

      {/* footer */}
      <div className="flex justify-center py-10 bg-gray-100 ">
        <input
          value={inputValue}
          onChange={handleChange}
          placeholder="Send a message..."
          className="transition ease-in-out delay-150  rounded-xl px-8 py-2 mx-20 focus:ring-2 focus:ring-green-500"
          style={{ width: "90%" }}
        />
        <button
          className=" transition ease-in-out delay-50 hover:bg-gray-200 relative bottom-2 right-12 mt-3 mr-3 text-gray-800 rounded-xl px-4 py-2"
          onClick={() => console.log("hello")}
        >
          Send ➤
        </button>
      </div>
    </main>
  );
}
