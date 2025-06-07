import './login.css'

import { AuthService } from '../../services/AuthService';
import { useNavigate } from 'react-router-dom';

import { FormEvent, useState } from 'react';
import { LoginResponse } from '../../models/LoginResponse';

export function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    async function handleLogin(e: FormEvent) {
        let authService: AuthService = new AuthService();

        e.preventDefault();
        setError('');

        try {
            let data: LoginResponse = await authService.login(email, password);
            localStorage.setItem('token', data.token);

            navigate('/dashboard');

        } catch (error) {
            setError('Erro no login')
        }
    }

    return (
        <div className="container">
            <div className="row min-vh-100 d-flex justify-content-center align-items-center">
                <div className="col-lg-5 col-md-7 col-sm-6 col-xs-12 mx-auto">
                    <div id="login-page">
                        <div id="login-container" className="container">
                            <h3>Acessar o administrativo.</h3>
                            <form id="login-form" onSubmit={handleLogin}>
                                <div className="form-group">
                                    <label htmlFor="email_id">E-mail</label>
                                    <input type="email" id="email_id" className="form-control" name="email_name" value={email} onChange={(e) => setEmail(e.target.value)} required/>
                                </div>
                                <div className="form-group mt-3">
                                    <label htmlFor="password_id">Senha</label>
                                    <input type="password" id="password_id" className="form-control" name="password_name" value={password} onChange={(e) => setPassword(e.target.value)} required/>
                                </div>
                                <div id="actions" className="mt-3 d-flex justify-content-between">
                                    <button type="submit" className="btn btn-vinil">Entrar</button>
                                    <small>
                                        <a href="#">Equeceu sua Senha</a>
                                    </small>
                                </div>
                                {error && <div className="alert alert-danger">{error}</div>}
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
