import { LoginResponse } from "../models/LoginResponse";
import { Service } from "./AbstractService";

export class AuthService extends Service {
    readonly URI: string = "/auth";

    public async login(email: string, password: string): Promise<LoginResponse> {
        let formatedURL: string = this.urlPrefix + this.URI;

        let payload = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ email, password}),
        }

        const response = await fetch(formatedURL, payload);
        const data = await response.json();

        if (!response.ok){
            throw new Error(data.message || 'Erro ao fazer login.');
        }

        return data;
    }
}