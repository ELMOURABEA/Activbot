#!/usr/bin/env python
"""
Activbot Demo - Demonstrates the auto-design workflow system
"""

from activbot import WorkflowEngine, WorkflowManager, PluginLoader


def demo_workflow_generation():
    """Demonstrate workflow auto-generation"""
    print("=" * 70)
    print("DEMO: Auto-Generate Workflow from Requirements")
    print("=" * 70)
    
    manager = WorkflowManager()
    
    requirements = {
        'name': 'demo_pipeline',
        'goals': [
            {'type': 'setup', 'description': 'Setup environment'},
            {'type': 'build', 'description': 'Build application', 'depends_on': ['task_1_setup']},
            {'type': 'test', 'description': 'Run comprehensive tests', 'depends_on': ['task_2_build']},
            {'type': 'package', 'description': 'Package artifacts', 'depends_on': ['task_3_test']},
            {'type': 'deploy', 'description': 'Deploy to staging', 'depends_on': ['task_4_package']}
        ]
    }
    
    print("\nRequirements:")
    for i, goal in enumerate(requirements['goals'], 1):
        print(f"  {i}. {goal['type']}: {goal['description']}")
    
    workflow = manager.generate_workflow_from_requirements(requirements)
    
    print(f"\n✓ Generated workflow: {workflow['name']}")
    print(f"  Version: {workflow['version']}")
    print(f"  Tasks: {len(workflow['tasks'])}")
    print(f"  Auto-generated: {workflow['metadata']['auto_generated']}")
    
    return workflow


def demo_workflow_update():
    """Demonstrate workflow update with version tracking"""
    print("\n" + "=" * 70)
    print("DEMO: Update Workflow with Version Control")
    print("=" * 70)
    
    manager = WorkflowManager()
    
    updates = {
        'description': 'Enhanced demo pipeline with retry logic',
        'tasks': [
            {'name': 'task_1_setup', 'type': 'setup', 'description': 'Setup environment', 'parameters': {}, 'depends_on': []},
            {'name': 'task_2_build', 'type': 'build', 'description': 'Build application', 'parameters': {}, 'depends_on': ['task_1_setup']},
            {'name': 'task_3_test', 'type': 'test', 'description': 'Run comprehensive tests', 'parameters': {}, 'depends_on': ['task_2_build'], 'retry': {'max_attempts': 3, 'delay': 5}},
            {'name': 'task_4_package', 'type': 'package', 'description': 'Package artifacts', 'parameters': {}, 'depends_on': ['task_3_test']},
            {'name': 'task_5_deploy', 'type': 'deploy', 'description': 'Deploy to staging', 'parameters': {'environment': 'staging'}, 'depends_on': ['task_4_package'], 'retry': {'max_attempts': 2, 'delay': 10}}
        ]
    }
    
    updated = manager.update_workflow('demo_pipeline', updates, 
                                     reason='Added retry logic for critical tasks')
    
    print(f"\n✓ Updated workflow: {updated['name']}")
    print(f"  Previous version: 1.0.0")
    print(f"  New version: {updated['version']}")
    print(f"  Update reason: {updated['update_history'][-1]['reason']}")
    
    return updated


def demo_workflow_execution():
    """Demonstrate workflow execution"""
    print("\n" + "=" * 70)
    print("DEMO: Execute Workflow")
    print("=" * 70)
    
    # Load plugins
    loader = PluginLoader()
    plugins = loader.load_all_plugins()
    
    # Create engine and register plugins
    engine = WorkflowEngine()
    for name, plugin in plugins.items():
        engine.register_plugin(name, plugin)
    
    # Load and execute simple workflow
    engine.load_workflow('activbot/workflows/simple_workflow.yml')
    print("\nExecuting simple_workflow...")
    
    results = engine.execute_workflow('simple_workflow')
    
    print(f"\n✓ Execution completed: {results['status']}")
    print(f"  Tasks executed: {len(results['tasks'])}")
    for task in results['tasks']:
        print(f"    - {task['name']}: {task['status']}")
    
    return results


def demo_validation():
    """Demonstrate workflow validation"""
    print("\n" + "=" * 70)
    print("DEMO: Validate Workflows")
    print("=" * 70)
    
    from activbot.validator import WorkflowValidator
    
    validator = WorkflowValidator()
    
    print("\nValidating all workflows...")
    results = validator.validate_all_workflows()
    
    for name, result in results.items():
        status = "✓ VALID" if result['valid'] else "✗ INVALID"
        print(f"  {status}: {name}")
        
        if not result['valid']:
            for error in result['errors']:
                print(f"    - {error}")
    
    return results


def demo_auto_analysis():
    """Demonstrate auto-analysis and improvement suggestions"""
    print("\n" + "=" * 70)
    print("DEMO: Auto-Analysis & Improvement Suggestions")
    print("=" * 70)
    
    from activbot.updater import WorkflowUpdater
    
    updater = WorkflowUpdater()
    
    print("\nAnalyzing workflows for improvements...")
    suggestions = updater.analyze_workflows()
    
    for workflow_name, workflow_suggestions in suggestions.items():
        print(f"\n  {workflow_name}:")
        if workflow_suggestions:
            for suggestion in workflow_suggestions:
                print(f"    - {suggestion}")
        else:
            print("    ✓ No improvements suggested")
    
    return suggestions


def main():
    """Run all demos"""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "ACTIVBOT AUTO-DESIGN WORKFLOW SYSTEM" + " " * 17 + "║")
    print("║" + " " * 21 + "Interactive Demonstration" + " " * 22 + "║")
    print("╚" + "═" * 68 + "╝")
    print()
    
    try:
        # Demo 1: Auto-generate workflow
        demo_workflow_generation()
        
        # Demo 2: Update workflow
        demo_workflow_update()
        
        # Demo 3: Execute workflow
        demo_workflow_execution()
        
        # Demo 4: Validate workflows
        demo_validation()
        
        # Demo 5: Auto-analysis
        demo_auto_analysis()
        
        print("\n" + "=" * 70)
        print("DEMO COMPLETED SUCCESSFULLY")
        print("=" * 70)
        print("\nThe Activbot system demonstrates:")
        print("  ✓ Dynamic workflow generation from requirements")
        print("  ✓ Version-controlled workflow updates")
        print("  ✓ Automated workflow execution")
        print("  ✓ Schema-based validation")
        print("  ✓ Self-analysis and improvement suggestions")
        print("\nActivbot is ready for continuous evolution! 🚀")
        print()
        
    except Exception as e:
        print(f"\n✗ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
