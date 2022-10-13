

CREATE TABLE IF NOT EXISTS BTC
Date,Open,High,Low,Close,Adj Close,Volume
(
    "Date" Date,
    "Open" FLOAT NOT NULL,
    "High" FLOAT NOT NULL,
    "Low" FLOAT NOT NULL,
    "Close" FLOAT NOT NULL,
    "Adj close" FLOAT NOT NULL,
    "Volume" FLOAT NOT NULL,
    PRIMARY KEY ("Date")
);