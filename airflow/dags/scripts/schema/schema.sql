

CREATE TABLE IF NOT EXISTS BTC
Date,Open,High,Low,Close,Adj Close,Volume
(
    "Date" DATE NOT NULL,
    "Open" float8 NOT NULL,
    "High" float8 NOT NULL,
    "Low" float8 NOT NULL,
    "Close" float8 NOT NULL,
    "Adj close" float8 NOT NULL,
    "Volume" float8 NOT NULL,
    PRIMARY KEY ("Date")
);