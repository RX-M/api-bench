#include "gen-cpp/Projects.h"
#include "gen-cpp/project_types.h"
#include <thrift/server/TThreadedServer.h>
#include <thrift/transport/TServerSocket.h>
#include <thrift/transport/TBufferTransports.h>
#include <thrift/protocol/TCompactProtocol.h>
#include <boost/program_options.hpp>
#include <boost/make_shared.hpp>
#include <boost/shared_ptr.hpp>
#include <iostream>

using namespace ::apache::thrift::server;
using namespace ::apache::thrift::protocol;
using namespace ::apache::thrift::transport;
using namespace OpenSourceProjects;
namespace po = boost::program_options;
using boost::shared_ptr;
using boost::make_shared;

//Projects service handler
class ProjectsHandler : public ProjectsIf {
public:
    ProjectsHandler() { 
        m_d.__set_year(2007);
        m_d.__set_month(1);
        m_d.__set_day(10);
    }
    virtual void get(Project& p, const std::string& name) {
        p.__set_name(name);
        p.__set_host("ASF");
        p.__set_inception(m_d);    }
    virtual void create(CreateResult& cr, const Project& proj) {
        cr.code = 200;
        cr.message = "OK";
    }
private:
    Date m_d;
};

int main(int argc, char* argv[]) {
    //Parse the command line
    int port = 9090;
    po::options_description desc("Allowed options");
    desc.add_options()
        ("port", po::value<int>(&port)->default_value(9090), "Port")
    ;
    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);  
    //Configure the I/O stack
    auto handler = make_shared<ProjectsHandler>();
    auto proc = make_shared<ProjectsProcessor>(handler);
    auto trans_svr = make_shared<TServerSocket>(port);
    auto trans_fac = make_shared<TBufferedTransportFactory>();
    auto proto_fac = make_shared<TCompactProtocolFactory>();
    TThreadedServer server(proc, trans_svr, trans_fac, proto_fac);
    std::cout << "[Server] Listening on port " << port << std::endl;
    server.serve();
    return 0;
}
