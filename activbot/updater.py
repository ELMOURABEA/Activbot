"""
Auto-Updater - Manages automatic updates and improvements to workflows
"""
import sys
from pathlib import Path
from typing import Dict, List, Any
import yaml
from datetime import datetime, timezone


class WorkflowUpdater:
    """
    Automatically analyzes and suggests improvements to workflows.
    Enables self-evolution of the workflow system.
    """
    
    def __init__(self, workflow_dir: str = "activbot/workflows",
                 plugin_dir: str = "activbot/plugins"):
        self.workflow_dir = Path(workflow_dir)
        self.plugin_dir = Path(plugin_dir)
        self._plugin_files_cache = None
        self._workflow_files_cache = None
        self._cache_timestamp = None
    
    def _get_plugin_files(self, use_cache: bool = True):
        """Get list of plugin files with optional caching."""
        import time
        
        current_time = time.time()
        if (use_cache and self._plugin_files_cache is not None and 
            self._cache_timestamp is not None and 
            current_time - self._cache_timestamp < 5):
            return self._plugin_files_cache
        
        plugin_files = [f for f in self.plugin_dir.glob("*.py") 
                       if not f.name.startswith("__")] if self.plugin_dir.exists() else []
        
        self._plugin_files_cache = plugin_files
        if self._cache_timestamp is None:
            self._cache_timestamp = current_time
        
        return plugin_files
    
    def _get_workflow_files(self, use_cache: bool = True):
        """Get list of workflow files with optional caching."""
        import time
        
        current_time = time.time()
        if (use_cache and self._workflow_files_cache is not None and 
            self._cache_timestamp is not None and 
            current_time - self._cache_timestamp < 5):
            return self._workflow_files_cache
        
        workflow_files = list(self.workflow_dir.glob("*.yml")) if self.workflow_dir.exists() else []
        
        self._workflow_files_cache = workflow_files
        if self._cache_timestamp is None:
            self._cache_timestamp = current_time
        
        return workflow_files
        
    def check_plugin_updates(self, use_cache: bool = True) -> Dict[str, Any]:
        """
        Check for available plugin updates.
        
        Args:
            use_cache: If True, use cached plugin file list
        
        Returns:
            Dictionary of plugin update information
        """
        updates = {}
        
        for plugin_file in self._get_plugin_files(use_cache):
            plugin_name = plugin_file.stem
            
            # Check plugin modification time
            mod_time = plugin_file.stat().st_mtime
            
            updates[plugin_name] = {
                'status': 'up-to-date',
                'last_modified': datetime.fromtimestamp(mod_time).isoformat(),
                'path': str(plugin_file)
            }
            
        return updates
        
    def analyze_workflows(self, use_cache: bool = True) -> Dict[str, List[str]]:
        """
        Analyze workflows for potential improvements.
        
        Args:
            use_cache: If True, use cached workflow file list
        
        Returns:
            Dictionary of workflow names to improvement suggestions
        """
        suggestions = {}
            
        for workflow_file in self._get_workflow_files(use_cache):
            with open(workflow_file, 'r') as f:
                workflow = yaml.safe_load(f)
                
            workflow_suggestions = []
            
            # Check for missing metadata
            if 'description' not in workflow:
                workflow_suggestions.append("Consider adding a description field")
                
            if 'version' not in workflow:
                workflow_suggestions.append("Consider adding version tracking")
                
            # Check task organization
            tasks = workflow.get('tasks', [])
            
            if len(tasks) > 10:
                workflow_suggestions.append(
                    "Large workflow detected - consider breaking into smaller workflows"
                )
                
            # Check for tasks without descriptions
            tasks_without_desc = [
                t.get('name') for t in tasks 
                if 'description' not in t
            ]
            
            if tasks_without_desc:
                workflow_suggestions.append(
                    f"Tasks without descriptions: {', '.join(tasks_without_desc)}"
                )
                
            # Check for retry logic
            tasks_without_retry = [
                t.get('name') for t in tasks 
                if t.get('type') in ['test', 'deployment', 'external_api'] 
                and 'retry' not in t
            ]
            
            if tasks_without_retry:
                workflow_suggestions.append(
                    f"Consider adding retry logic to: {', '.join(tasks_without_retry)}"
                )
                
            # Check for dependency optimization
            independent_tasks = [
                t.get('name') for t in tasks 
                if 'depends_on' not in t or not t['depends_on']
            ]
            
            if len(independent_tasks) > 1:
                workflow_suggestions.append(
                    f"Tasks that can run in parallel: {', '.join(independent_tasks)}"
                )
                
            suggestions[workflow_file.name] = workflow_suggestions
            
        return suggestions
        
    def generate_update_report(self) -> str:
        """
        Generate a comprehensive update report.
        
        Returns:
            Formatted report string
        """
        report_lines = [
            "=" * 60,
            "ACTIVBOT AUTO-UPDATE REPORT",
            "=" * 60,
            f"Generated: {datetime.now(timezone.utc).isoformat()}",
            "",
        ]
        
        # Plugin updates section
        report_lines.extend([
            "PLUGIN STATUS",
            "-" * 60,
        ])
        
        plugin_updates = self.check_plugin_updates()
        if plugin_updates:
            for plugin_name, info in plugin_updates.items():
                report_lines.append(f"  {plugin_name}: {info['status']}")
                report_lines.append(f"    Last modified: {info['last_modified']}")
        else:
            report_lines.append("  No plugins found")
            
        report_lines.append("")
        
        # Workflow improvements section
        report_lines.extend([
            "WORKFLOW IMPROVEMENT SUGGESTIONS",
            "-" * 60,
        ])
        
        workflow_suggestions = self.analyze_workflows()
        if workflow_suggestions:
            for workflow_name, suggestions in workflow_suggestions.items():
                report_lines.append(f"  {workflow_name}:")
                
                if suggestions:
                    for suggestion in suggestions:
                        report_lines.append(f"    - {suggestion}")
                else:
                    report_lines.append("    ✓ No improvements suggested")
                    
                report_lines.append("")
        else:
            report_lines.append("  No workflows found")
            
        report_lines.extend([
            "=" * 60,
            "END OF REPORT",
            "=" * 60,
        ])
        
        return "\n".join(report_lines)
        
    def apply_auto_updates(self, dry_run: bool = True) -> Dict[str, Any]:
        """
        Apply automatic updates to workflows (when safe to do so).
        
        Args:
            dry_run: If True, only simulate updates without applying
            
        Returns:
            Dictionary of applied updates
        """
        updates_applied = {
            'workflows_updated': [],
            'plugins_updated': [],
            'dry_run': dry_run
        }
        
        # In a real implementation, this would:
        # 1. Check for safe, non-breaking updates
        # 2. Apply version bumps to workflows
        # 3. Add missing recommended fields
        # 4. Update plugin dependencies
        
        return updates_applied


def main():
    """Command-line interface for workflow updater."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Activbot Auto-Updater')
    parser.add_argument('--check-plugins', action='store_true',
                       help='Check for plugin updates')
    parser.add_argument('--analyze-workflows', action='store_true',
                       help='Analyze workflows for improvements')
    parser.add_argument('--report', action='store_true',
                       help='Generate full update report')
    parser.add_argument('--apply-updates', action='store_true',
                       help='Apply automatic updates (use with caution)')
    parser.add_argument('--dry-run', action='store_true', default=True,
                       help='Simulate updates without applying (default: true)')
    
    args = parser.parse_args()
    
    updater = WorkflowUpdater()
    
    if args.check_plugins:
        print("Checking plugin status...")
        updates = updater.check_plugin_updates()
        
        for plugin_name, info in updates.items():
            print(f"  {plugin_name}: {info['status']}")
            
    elif args.analyze_workflows:
        print("Analyzing workflows...")
        suggestions = updater.analyze_workflows()
        
        for workflow_name, workflow_suggestions in suggestions.items():
            print(f"\n{workflow_name}:")
            if workflow_suggestions:
                for suggestion in workflow_suggestions:
                    print(f"  - {suggestion}")
            else:
                print("  ✓ No improvements suggested")
                
    elif args.report:
        report = updater.generate_update_report()
        print(report)
        
    elif args.apply_updates:
        print("Applying automatic updates...")
        results = updater.apply_auto_updates(dry_run=args.dry_run)
        
        if results['dry_run']:
            print("DRY RUN - No changes applied")
        else:
            print(f"Updated {len(results['workflows_updated'])} workflows")
            print(f"Updated {len(results['plugins_updated'])} plugins")
            
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
