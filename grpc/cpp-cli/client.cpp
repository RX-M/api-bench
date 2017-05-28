#include "projects.pb.h"
#include "projects.grpc.pb.h"
#include <grpc++/create_channel.h>
#include <grpc++/security/credentials.h>
#include <boost/program_options.hpp>
#include <iostream>
#include <string>

namespace po = boost::program_options;

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

    auto channel = grpc::CreateChannel(host + ":" + std::to_string(port), grpc::InsecureChannelCredentials());
    grpc::ClientContext context;
    auto stub = OpenSourceProjects::Projects::NewStub(channel);

    OpenSourceProjects::Project p;
    auto date = p.mutable_inception();
    date->set_year(2007);
    date->set_month(1);
    date->set_day(10);
    OpenSourceProjects::GetArg name;
    name.set_name("Thrift");
    OpenSourceProjects::CreateResult cr;

    switch (action) {
    case 1:
      for (int i = 0; i < 1000000; i++) {
        auto status = stub->Get(&context, name, &p);
        if (!status.ok()) {
          std::cout << std::endl;
          return 1;
        }
      }
      break;
    case 2:
      for (int i = 0; i < 1000000; i++) {
        auto status = stub->Create(&context, p, &cr);
        if (!status.ok()) {
          std::cout << std::endl;
          return 1;
        }
      }
      break;
    case 3:
      for (int i = 0; i < 1000000; i++) {
        auto status = stub->Create(&context, p, &cr);
        if (!status.ok()) {
          std::cout << std::endl;
          return 1;
        }
        status = stub->Get(&context, name, &p);
        if (!status.ok()) {
          std::cout << status.error_message() << std::endl;
          return 1;
        }
      }
      break;
    }
}
