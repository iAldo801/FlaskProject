'use client'

import { useEffect, useState } from "react";

interface Data {
  message: string;
}

export default function Home() {

  const [data, setData] = useState<Data>();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8080/api/user');
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <main className="flex justify-center items-center min-h-svh text-4xl text-white">
      <div>
        <h1>Flask (Python) API Fetch</h1>
        {data ? (
          <pre>
            {data.message}
          </pre>
        ) : (
          <p>Loading...</p>
        )}
      </div>
    </main>
  );
}