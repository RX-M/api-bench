TARGET = client
IDL = ../project.thrift
CLISRC = client.cpp gen-cpp/Projects.cpp gen-cpp/project_types.cpp

CC = g++
LIBS = -lthrift -lboost_program_options
CFLAGS = -Wall -std=c++11
THRIFT = thrift -gen cpp

all: client

gen-cpp/Projects.cpp: $(IDL)
	$(THRIFT) $(IDL)

gen-cpp/project_types.cpp: $(IDL)
	$(THRIFT) $(IDL)

client: $(CLISRC)
	$(CC) -o $@ $(CLISRC) $(CFLAGS) $(LIBS)
	
clean:
	$(RM) -r gen-cpp
	$(RM) $(TARGET)
