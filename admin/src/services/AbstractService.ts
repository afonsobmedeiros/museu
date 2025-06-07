export abstract class Service {
    public get urlPrefix(): string {
        if (process.env.NODE_ENV !== 'production') {
            return 'http://127.0.0.1:8080';
        } else {
            return '';
        }
    }
}
