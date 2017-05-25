TARGET = server
IDL = ../project.thrift
SVRSRC = nb_server.cpp gen-cpp/TradeHistory.cpp gen-cpp/trade_report_types.cpp

CC = g++
LIBS = -lthrift -lthriftnb -levent
CFLAGS = -Wall -std=c++11
THRIFT = thrift -gen cpp

all: server 

gen-cpp/Reports.cpp: $(IDL)
	$(THRIFT) $(IDL)

gen-cpp/reports.cpp: $(IDL)
	$(THRIFT) $(IDL)

server: $(SVRSRC)
	$(CC) -o $@ $(SVRSRC) $(CFLAGS) $(LIBS)

clean:
	$(RM) -r gen-cpp
	$(RM) $(TARGET)
