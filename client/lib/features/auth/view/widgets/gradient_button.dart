import 'package:client/core/theme/app_pallet.dart';
import 'package:flutter/material.dart';

class GradientButton extends StatelessWidget {
  final String buttonText;
  final VoidCallback onTap;

  const GradientButton({
    super.key,
    required this.buttonText,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          colors: [Pallet.gradient1, Pallet.gradient2],
          begin: AlignmentGeometry.bottomLeft,
          end: AlignmentGeometry.topRight,
        ),
        borderRadius: BorderRadius.circular(5),
      ),
      child: ElevatedButton(
        onPressed: onTap,
        style: ElevatedButton.styleFrom(
          fixedSize: Size(MediaQuery.of(context).size.width, 55),
          backgroundColor: Pallet.transparentColor,
          shadowColor: Pallet.transparentColor,
        ),
        child: Text(
          buttonText,
          style: TextStyle(fontSize: 17, fontWeight: FontWeight.w600),
        ),
      ),
    );
  }
}
