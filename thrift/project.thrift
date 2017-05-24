// Apache Thrift IDL for the RX-M LLC LinuxCon Open Source Demonstration App
//
// This interface allows users to get and update open source project information

namespace * OpenSourceProjects

struct Date {
    1: i16  year
    2: i16  month
    3: i16  day
} 


struct Project {
    1: string name       //Proper project name
    2: string host       //Hosting/control foundation or company
    3: Date inception    //Date project was open sourced
}

struct CreateResult {
    1: i16 code
    2: string message
}

service Projects {
    Project get(1: string name)
    CreateResult create(1: Project proj)
}
