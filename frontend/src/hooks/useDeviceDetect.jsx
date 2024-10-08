import { useState, useEffect } from "react"

export const useDeviceDetect = () => {
    const [device, setDevice] = useState('pc')
    const handleResize = () => {
        const width = window.innerWidth

        if(width < 768){
          setDevice('mobile')
        }
        else if(width < 992){
          setDevice('tablet')
        }
        else{
          setDevice('pc')
        }
    }
    

    useEffect(() => {
        handleResize()
        window.addEventListener('resize', handleResize)
        return () => window.addEventListener('resize', handleResize)
    }, [])
    return {device}
  }