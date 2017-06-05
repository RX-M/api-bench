#include "projects.pb.h"
#include "projects.grpc.pb.h"
#include <grpc++/server.h>
#include <grpc++/server_builder.h>
#include <boost/program_options.hpp>
#include <memory>
#include <string>

namespace po = boost::program_options;

class ProjectsService final : public OpenSourceProjects::Projects::Service {
  public:
    ::grpc::Status Get(::grpc::ServerContext*, const ::OpenSourceProjects::GetArg* request, ::OpenSourceProjects::Project* response) override {
      response->set_name(request->name());
      response->set_host("ASF");
      auto inception = response->mutable_inception();
      inception->set_year(2017);
      inception->set_month(1);
      inception->set_day(10);
      return grpc::Status::OK;
    }

    ::grpc::Status Create(::grpc::ServerContext*, const ::OpenSourceProjects::Project*, ::OpenSourceProjects::CreateResult* response) override {
      response->set_code(200);
      response->set_message("OK");
      return grpc::Status::OK;
    }
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

    ProjectsService service;
    auto server_address = std::string("localhost:") + std::to_string(port);

    grpc::ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::unique_ptr<grpc::Server> server(builder.BuildAndStart());
    std::cout << "[Server] Listening on " << server_address << std::endl;
    server->Wait();
}
