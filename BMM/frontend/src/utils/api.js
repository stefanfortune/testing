import {useAuth} from "@clerk/clerk-react"

export const useApi = () => {
    const {getToken} = useAuth()

    const makeRequest = async (endpoint, options = {}) => {
        try {
            const token = await getToken()
            
            if (!token) {
                throw new Error("No authentication token available")
            }

            const defaultOptions = {
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                }
            }

            const response = await fetch(`http://localhost:8000/api/${endpoint}`, {
                ...defaultOptions,
                ...options,
                headers: {
                    ...defaultOptions.headers,
                    ...options.headers
                }
            })
            
            if (!response.ok) {
                const errorData = await response.json().catch(() => null)
                console.error(`API Error ${response.status}:`, errorData)
                
                if (response.status === 401) {
                    throw new Error("Authentication failed. Please sign in again.")
                }
                if (response.status === 429) {
                    throw new Error("Daily quota exceeded")
                }
                if (response.status === 404) {
                    throw new Error("Resource not found")
                }
                throw new Error(errorData?.detail || `Server error: ${response.status}`)
            }

            return response.json()
        } catch (error) {
            console.error("API request failed:", error)
            throw error
        }
    }

    return {makeRequest}
}