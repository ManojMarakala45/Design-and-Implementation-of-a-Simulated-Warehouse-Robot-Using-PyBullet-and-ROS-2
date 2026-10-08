from setuptools import setup

package_name = "warehouse_robot"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    description="Warehouse robot mission controller and keyboard HRI",
    license="Apache-2.0",
    entry_points={
        "console_scripts": [
            "mission_controller = warehouse_robot.mission_controller:main",
            "keyboard_hri = warehouse_robot.keyboard_hri:main",
        ],
    },
)
