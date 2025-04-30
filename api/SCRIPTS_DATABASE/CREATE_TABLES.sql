CREATE TABLE IF NOT EXISTS Curators(
	Id INTEGER PRIMARY KEY AUTO_INCREMENT,
	Name VARCHAR(50) Not null,
	Email VARCHAR(100) Not null UNIQUE,
	password VARCHAR(256) Not null,
	Type INTEGER,
	Created_at DATETIME Default Current_TimeStamp,
	Updated_at DATETIME Default Current_TimeStamp On Update Current_TimeStamp
);


CREATE TABLE IF NOT EXISTS Exhibitions(
	Id INTEGER PRIMARY KEY AUTO_INCREMENT,
	Name VARCHAR(50) Not null,
	Summary VARCHAR(100),
	Start_at DATETIME Not null,
	Finish_at DATETIME Not null,
	Created_at DATETIME Default Current_TimeStamp,
	Updated_at DATETIME Default Current_TimeStamp On Update Current_TimeStamp,
	CuratorId Integer Not null,
	Foreign Key (CuratorId) References Curators(Id)
);

CREATE TABLE IF NOT EXISTS Collections(
	Id INTEGER PRIMARY KEY AUTO_INCREMENT,
	Name VARCHAR(50) Not null,
	Summary VARCHAR(100),
	Created_at DATETIME Default Current_TimeStamp,
	Updated_at DATETIME Default Current_TimeStamp On Update Current_TimeStamp,
	ExhibitionId Integer Not null,
	Foreign Key (ExhibitionId) References Exhibitions(Id)
);

CREATE TABLE IF NOT EXISTS Pieces(
	Id INTEGER PRIMARY KEY AUTO_INCREMENT,
	Subtitle VARCHAR(50) Not null,
	Summary VARCHAR(100),
	PartDate Date,
	photo TEXT,
	photoPath TEXT,
	Created_at DATETIME Default Current_TimeStamp,
	Updated_at DATETIME Default Current_TimeStamp On Update Current_TimeStamp,
	CollectionId Integer Not null,
	Foreign Key (CollectionId ) References Collections(Id)
);