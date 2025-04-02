import 'package:flutter/material.dart';
import 'package:practice_hecns/service/service.dart';

class CodePage extends StatelessWidget {
  final int wardNumber;
  CodePage({super.key, required this.wardNumber});

  // List of predefined emergency codes with corresponding colors
  final List<Map<String, dynamic>> emergencyCodes = [
    {"name": "Code Blue", "color": Colors.blue},
    {"name": "Code Red", "color": Colors.red},
    {"name": "Code Yellow", "color": Colors.yellow},
    {"name": "Code Black", "color": Colors.black},
    {"name": "Code White", "color": Colors.white}
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Ward $wardNumber - Emergency Codes'),
        backgroundColor: const Color.fromRGBO(39, 201, 201, 1),
        elevation: 0,
      ),
      body: ListView.builder(
        itemCount: emergencyCodes.length,
        itemBuilder: (context, index) {
          return Container(
            color: emergencyCodes[index]["color"],
            child: ListTile(
              title: Text(
                '${emergencyCodes[index]["name"]} - Ward $wardNumber',
                style: TextStyle(
                  color: emergencyCodes[index]["color"] == Colors.black
                      ? Colors.white
                      : Colors.black, // Adjust text color for readability
                ),
              ),
              trailing: const Icon(Icons.info_outline, color: Colors.black),
              onTap: () {
                UserService userService = UserService();
                  userService.sendMessage("Hospital Emergency ${emergencyCodes[index]["name"]} Ward $wardNumber");
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text('Selected ${emergencyCodes[index]["name"]} for Ward $wardNumber')),
                );
              },
            ),
          );
        },
      ),
    );
  }
}