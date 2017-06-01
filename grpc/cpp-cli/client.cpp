#include "projects.pb.h"
#include "projects.grpc.pb.h"
#include <grpc++/create_channel.h>
#include <grpc++/security/credentials.h>
#include <boost/program_options.hpp>
#include <chrono>
#include <iostream>
#include <string>

namespace po = boost::program_options;

int main(int argc, char* argv[]) {
    //Parse the command line
    int port = 9090;
    int action = 1;
    int repeat = 1000000;
    std::string host = "localhost";
    po::options_description desc("Allowed options");
    desc.add_options()
        ("host", po::value<std::string>(&host)->default_value("localhost"), "Host")
        ("port", po::value<int>(&port)->default_value(9090), "Port")
        ("action", po::value<int>(&action)->default_value(1), "Test Action (must be 1, 2 or 3)")
        ("repeat", po::value<int>(&repeat)->default_value(1000000), "Number of requests")
    ;
    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);

    auto channel = grpc::CreateChannel(host + ":" + std::to_string(port), grpc::InsecureChannelCredentials());
    auto stub = OpenSourceProjects::Projects::NewStub(channel);

    OpenSourceProjects::Project p;
    auto date = p.mutable_inception();
    date->set_year(2007);
    date->set_month(1);
    date->set_day(10);
    OpenSourceProjects::GetArg name;
    name.set_name("Thrift");
    OpenSourceProjects::CreateResult cr;

    auto begin = std::chrono::high_resolution_clock::now();
    std::cout << "Time to ";
    switch (action) {
    case 1:
      std::cout << "Get() ";
      for (int i = 0; i < repeat; i++) {
        grpc::ClientContext context;
        auto status = stub->Get(&context, name, &p);
        if (!status.ok()) {
          std::cout << "Get failed: " << status.error_message() << std::endl;
          return 1;
        }
      }
      break;
    case 2:
      std::cout << "Create() ";
      for (int i = 0; i < repeat; i++) {
        grpc::ClientContext context;
        auto status = stub->Create(&context, p, &cr);
        if (!status.ok()) {
          std::cout << "Create failed: " << status.error_message() << std::endl;
          return 1;
        }
      }
      break;
    case 3:
      std::cout << "Create() then Get() ";
      for (int i = 0; i < repeat; i++) {
        grpc::ClientContext context;
        auto status = stub->Create(&context, p, &cr);
        if (!status.ok()) {
          std::cout << "Create failed: " << status.error_message() << std::endl;
          return 1;
        }
        grpc::ClientContext context2;
        status = stub->Get(&context2, name, &p);
        if (!status.ok()) {
          std::cout << "Get failed: " << status.error_message() << std::endl;
          return 1;
        }
      }
      break;
    }
    auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::high_resolution_clock::now() - begin);
    std::cout << repeat << " times: " << elapsed.count() << " ms " << std::endl;
}
