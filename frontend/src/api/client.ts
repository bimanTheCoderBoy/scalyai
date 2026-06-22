import axios from "axios";
import { API_URL } from "@/constants";

const apiClient = axios.create({
    baseURL: API_URL,
})

let tokenGetter: (() => Promise<string | null>) | null = null;

export const setTokenGetter = (getter: () => Promise<string | null>) => {
    tokenGetter = getter;
};

apiClient.interceptors.request.use(async (config) => {
    if(tokenGetter) {
        const token = await tokenGetter();
        if(token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
    }
    return config;
})

export {
    apiClient,
}