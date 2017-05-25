TARGET = server
IDL = ../project.thrift
SRC = server.cpp gen-cpp/Projects.cpp gen-cpp/project_types.cpp

CC = g++
LIBS = -lthrift -lboost_program_options
CFLAGS = -Wall -std=c++11
THRIFT = thrift -gen cpp

all: server

gen-cpp/Projects.cpp: $(IDL)
	$(THRIFT) $(IDL)

gen-cpp/project_types.cpp: $(IDL)
	$(THRIFT) $(IDL)

server: $(SRC)
	$(CC) -o $@ $(SRC) $(CFLAGS) $(LIBS)
	
clean:
	$(RM) -r gen-cpp
	$(RM) $(TARGET)
