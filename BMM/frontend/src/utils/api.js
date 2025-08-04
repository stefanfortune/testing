import {useAuth} from "@clerk/clerk-react"

export const useApi = () => {
    const {getToken} = useAuth()

    const makeRequest = async (endpoint, options = {}) => {
        try {
            console.log(`Making request to: ${endpoint}`)
            const token = await getToken()
            console.log(`Token available: ${!!token}`)
            
            if (!token) {
                throw new Error("No authentication token available")
            }

            const defaultOptions = {
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                }
            }

            const url = `http://localhost:8000/api/${endpoint}`
            console.log(`Full URL: ${url}`)
            
            const response = await fetch(`http://localhost:8000/api/${endpoint}`, {
                ...defaultOptions,
                ...options,
                headers: {
                    ...defaultOptions.headers,
                    ...options.headers
                }
            })
            
            console.log(`Response status: ${response.status}`)
            
            if (!response.ok) {
                const errorData = await response.json().catch(() => null)
                console.error(`API Error ${response.status}:`, errorData)
                
                if (response.status === 401) {
                    throw new Error("Authentication failed. Please sign in again.")
                }
                if (response.status === 400) {
                    throw new Error(errorData?.detail || "Bad request")
                }
                if (response.status === 429) {
                    throw new Error("Daily quota exceeded")
                }
                if (response.status === 404) {
                    throw new Error("Resource not found")
                }
                throw new Error(errorData?.detail || `Server error: ${response.status}`)
            }

            const data = await response.json()
            console.log(`Response data:`, data)
            return data
        } catch (error) {
            console.error("API request failed:", error)
            throw error
        }
    }

    return {makeRequest}
}