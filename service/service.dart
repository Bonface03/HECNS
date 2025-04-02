import 'package:http/http.dart' as http;
import 'dart:convert'; // Import for jsonEncode

class UserService {
  String apiUrl = "http://172.16.14.251:5001"; // Corrected URL

  Future<bool> signInUser(String password, String username) async {
    try {
      final response = await http.post(
        Uri.parse('$apiUrl/login'),
        body: jsonEncode({
          'username': username,
          'password': password,
        }),
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
      );

      print("Login Response: ${response.body}");

      if (response.statusCode == 200) {
        return true;
      } else {
        return false;
      }
    } catch (e) {
      print("Error during login: $e");
      return false;
    }
  }

  Future<bool> sendMessage(String message) async {
    try {
      final response = await http.post(
        Uri.parse('$apiUrl/message'),
        body: jsonEncode({
          'word': message, 
        }),
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
      );

      print("Message Response: ${response.body}");

      if (response.statusCode == 200) {
        return true;
      } else {
        return false;
      }
    } catch (e) {
      print("Error sending message: $e");
      return false;
    }
  }
}
