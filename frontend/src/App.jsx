import { useState } from 'react'
import './App.css'
import axios from 'axios'

function App() {
  const [text, setText] = useState('')
  const [spam, setSpam] = useState("")

  const checkHandler = async() => {  
    try {
      if(text === ''){
        return
      }
      const res = await axios.post('http://127.0.0.1:8000', {sentence:text})
      console.log(res.data)
      setSpam(res.data)
      setText('')
    } catch (error) {
      console.log(error)
    }
  }

  return (
    <div className='bg-neutral-800 w-full h-screen text-white p-24 flex flex-col items-center'>
      <div className='text-7xl text-stone-500 flex justify-center m-6'>Spam Checker </div>
      <div className='flex flex-col bg-gray-900 rounded-sm justify-center items-center p-4 w-1/2 '> 
        <textarea 
          className='bg-neutral-700 text-white p-4 w-full outline-none border-none rounded-md' 
          placeholder='Enter text here' 
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <button onClick={checkHandler} className='bg-blue-900 hover:opacity-80 text-white p-4 w-full rounded-md mt-4'>Check</button>
      </div>
      {
        spam && (
          <h1 className={`flex justify-center text-3xl ${spam === "Spam"?"text-red-600":"text-green-600"}`}>
            {spam}
          </h1>
        )
      }
    </div>
  )
}

export default App
