import './dashboard.css'

export function Dashboard() {
  return (
    <div id="dashboard-page" className="container mt-5">
      <h1>Bem-vindo ao painel administrativo!</h1>
      <p>Conteúdo protegido para usuários logados.</p>
      <div className="container mb-4">
        <div className="row">
          <div className="col-md-6 col-sm-12 col-xs-12 col-lg-6">
            <a href="/exhibitions">
              <div className="link-nav">
                <h3>Exibições</h3>
              </div>
            </a>
          </div>
          <div className="col-md-6 col-sm-12 col-xs-12 col-lg-6">
            <a href="/collections">
              <div className="link-nav">
                <h3>Coleções</h3>
              </div>
            </a>
          </div>
          <div className="col-md-6 col-sm-12 col-xs-12 col-lg-6">
            <a href="/pieces">
              <div className="link-nav">
                <h3>Peças</h3>
              </div>
            </a>
          </div>
          <div className="col-md-6 col-sm-12 col-xs-12 col-lg-6">
            <a href="/curators">
              <div className="link-nav">
                <h3>Curadores</h3>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}