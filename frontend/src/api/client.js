import axios from "axios";
export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";
export const api = axios.create({ baseURL: API_BASE_URL });
export async function uploadResume(file){ const formData=new FormData(); formData.append("file",file); const r=await api.post("/api/v1/resumes/upload",formData,{headers:{"Content-Type":"multipart/form-data"}}); return r.data; }
export async function createJob(payload){ const r=await api.post("/api/v1/jobs",payload); return r.data; }
export async function runAnalysis(payload){ const r=await api.post("/api/v1/analysis/run",payload); return r.data; }
