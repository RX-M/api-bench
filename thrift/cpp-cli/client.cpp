#include "gen-cpp/Projects.h"
#include "gen-cpp/project_types.h"
#include <thrift/Thrift.h>
#include <thrift/transport/TSocket.h>
#include <thrift/transport/TBufferTransports.h>
#include <thrift/protocol/TCompactProtocol.h>
#include <boost/make_shared.hpp>
#include <boost/shared_ptr.hpp>
#include <boost/program_options.hpp>
#include <iostream>
#include <string>


using namespace apache::thrift;
using namespace apache::thrift::transport;
using namespace apache::thrift::protocol;
using namespace OpenSourceProjects;
namespace po = boost::program_options;
using boost::shared_ptr;
using boost::make_shared;

int main(int argc, char* argv[]) {
    //Parse the command line
    int port = 9090;
    int action = 1;
    std::string host = "localhost";
    po::options_description desc("Allowed options");
    desc.add_options()
        ("host", po::value<std::string>(&host)->default_value("localhost"), "Host")
        ("port", po::value<int>(&port)->default_value(9090), "Port")
        ("action", po::value<int>(&action)->default_value(1), "Test Action (must be 1, 2 or 3)")
    ;
    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);  
    //Setup the Thrift I/O stack
    auto trans_ep = make_shared<TSocket>(host.c_str(), port);
    auto trans = make_shared<TBufferedTransport>(trans_ep);
    auto proto = make_shared<TCompactProtocolT<TBufferedTransport>>(trans);
    ProjectsClient client(proto);
    std::cout << "[Client] Host " << host << ", Port " << port << ", Action " << action << std::endl;
    //Run the test
    try {
        trans->open();
        Date d;
        d.__set_year(2007);
        d.__set_month(1);
        d.__set_day(10);
        Project p;
        p.__set_name("Thrift");
        p.__set_host("ASF");
        p.__set_inception(d);
        CreateResult cr;
        std::string name = "Thrift";
        switch (action) {
        case 1:
            for (int i = 0; i < 1000000; i++)
                client.get(p, name);
            break;
        case 2:
            for (int i = 0; i < 1000000; i++)
                client.create(cr, p);
            break;
        case 3:
            for (int i = 0; i < 1000000; i++)
                client.create(cr, p);
                client.get(p, name);
            break;
        }
    } catch(const TTransportException& te) {
        std::cout << "Client caught a TTransportException: " << te.what() << std::endl;
    } catch(const TException& e) {
        std::cout << "Client caught a TException: " << e.what() << std::endl;
    } catch(...) {
        std::cout << "Client caught an exception" << std::endl;
    } 
    trans->close();
}
