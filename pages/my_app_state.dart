import 'package:flutter/material.dart';
import 'package:practice_hecns/pages/my_home_page.dart';

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}
class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Bonface',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: const Color.fromARGB(255, 117, 39, 201)),
      ),
      home: const MyHomePage(title: 'Hospital Code Notification System'),
    );
  }
}