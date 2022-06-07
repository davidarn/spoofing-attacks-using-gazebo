#include <gnc_functions.hpp>
#include <string>
#include <iostream>
#include <unistd.h>
//include API 

int main(int argc, char** argv)
{
	//initialize ros 
	ros::init(argc, argv, "gnc_node");
	ros::NodeHandle gnc_node("~");
	
	//initialize control publisher/subscribers
	init_publisher_subscriber(gnc_node);

  	// wait for FCU connection
	wait4connect();

	//wait for used to switch to mode GUIDED
	wait4start();

	//create local reference frame 
	initialize_local_frame();

	// request takeoff
	takeoff(3);

    std::cout << "\nTakeoff successfully carried out. ";

	//to give time to the user to execute the odometry attack
	char proceed{}; // default initialize to false
	std::cout << "\nDo you want to proceed? [y/n] ";
	std::cin >> proceed;
	if(!(proceed == 'y' || proceed == 'Y')){
		return 0;
	}

	std::vector<gnc_api_waypoint> waypointList;
	gnc_api_waypoint nextWayPoint;
	nextWayPoint.x = 5;
	nextWayPoint.y = 0;
	nextWayPoint.z = 0;
	nextWayPoint.psi = 0;
	waypointList.push_back(nextWayPoint);

	nextWayPoint.x = 5;
	nextWayPoint.y = 0;
	nextWayPoint.z = 3;
	nextWayPoint.psi = -90;
	waypointList.push_back(nextWayPoint);

	nextWayPoint.x = 5;
	nextWayPoint.y = 5;
	nextWayPoint.z = 3;
	nextWayPoint.psi = 0;
	waypointList.push_back(nextWayPoint);

	nextWayPoint.x = 0;
	nextWayPoint.y = 5;
	nextWayPoint.z = 3;
	nextWayPoint.psi = 90;
	waypointList.push_back(nextWayPoint);

	nextWayPoint.x = 0;
	nextWayPoint.y = 0;
	nextWayPoint.z = 3;
	nextWayPoint.psi = 180;
	waypointList.push_back(nextWayPoint);

	std::cout << "\nWaypoint procedure starts\n";

	ros::Rate rate(2.0);
	int counter = 0;
	while(ros::ok())
	{
		ros::spinOnce();
		rate.sleep();
		std::cout << "\nCheck if waypoint has been reached\n";
		if(check_waypoint_reached(.3) == 1)
		{
			if (counter < waypointList.size())
			{
				std::cout << "\nSet next waypoint\n";
				set_destination(waypointList[counter].x,waypointList[counter].y,waypointList[counter].z, waypointList[counter].psi);
				counter++;	
			}else{
				// land after all waypoints are reached
				land();
			}	
		}	
		
	}
	return 0;
}
