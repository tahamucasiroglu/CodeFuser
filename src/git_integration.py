import subprocess
import os
from pathlib import Path
from typing import List, Dict, Set, Optional, Tuple
from datetime import datetime, timedelta


class GitIntegration:
    def __init__(self, config_manager):
        self.config_manager = config_manager
    
    def is_git_repository(self, directory: Path) -> bool:
        """Check if directory is a git repository"""
        try:
            result = subprocess.run(
                ['git', 'rev-parse', '--git-dir'],
                cwd=str(directory),
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            return False
    
    def get_git_status(self, directory: Path) -> Dict[str, List[str]]:
        """Get git status of files"""
        if not self.is_git_repository(directory):
            return {}
        
        try:
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=str(directory),
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                return {}
            
            status = {
                'modified': [],
                'added': [],
                'deleted': [],
                'renamed': [],
                'untracked': [],
                'staged': []
            }
            
            for line in result.stdout.strip().split('\n'):
                if not line:
                    continue
                
                status_code = line[:2]
                filename = line[3:].strip()
                
                # Handle renamed files
                if '->' in filename:
                    old_name, new_name = filename.split(' -> ')
                    status['renamed'].append(new_name.strip())
                    filename = new_name.strip()
                
                # Check staged status (first character)
                if status_code[0] in ['A', 'M', 'D', 'R', 'C']:
                    status['staged'].append(filename)
                
                # Check working directory status (second character)
                if status_code[1] == 'M':
                    status['modified'].append(filename)
                elif status_code[1] == 'D':
                    status['deleted'].append(filename)
                elif status_code[0] == 'A':
                    status['added'].append(filename)
                elif status_code[0] == 'R':
                    status['renamed'].append(filename)
                elif status_code == '??':
                    status['untracked'].append(filename)
            
            return status
            
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as e:
            print(f"Git status error: {e}")
            return {}
    
    def get_changed_files_since(self, directory: Path, since: str = "HEAD~1") -> List[str]:
        """Get files changed since a specific commit/branch"""
        if not self.is_git_repository(directory):
            return []
        
        try:
            # Get files changed since specified commit
            result = subprocess.run(
                ['git', 'diff', '--name-only', since],
                cwd=str(directory),
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                return []
            
            files = [f.strip() for f in result.stdout.strip().split('\n') if f.strip()]
            return files
            
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as e:
            print(f"Git diff error: {e}")
            return []
    
    def get_changed_files_by_time(self, directory: Path, hours: int = 24) -> List[str]:
        """Get files changed in the last N hours"""
        if not self.is_git_repository(directory):
            return []
        
        try:
            # Calculate time threshold
            since_time = datetime.now() - timedelta(hours=hours)
            since_str = since_time.strftime('%Y-%m-%d %H:%M:%S')
            
            result = subprocess.run(
                ['git', 'log', '--name-only', '--pretty=format:', f'--since={since_str}'],
                cwd=str(directory),
                capture_output=True,
                text=True,
                timeout=15
            )
            
            if result.returncode != 0:
                return []
            
            files = set()
            for line in result.stdout.strip().split('\n'):
                if line.strip() and not line.startswith('commit'):
                    files.add(line.strip())
            
            return list(files)
            
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as e:
            print(f"Git log error: {e}")
            return []
    
    def get_branch_info(self, directory: Path) -> Dict[str, str]:
        """Get current branch and remote info"""
        if not self.is_git_repository(directory):
            return {}
        
        info = {}
        
        try:
            # Get current branch
            result = subprocess.run(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                cwd=str(directory),
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                info['branch'] = result.stdout.strip()
            
            # Get remote URL
            result = subprocess.run(
                ['git', 'config', '--get', 'remote.origin.url'],
                cwd=str(directory),
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                info['remote'] = result.stdout.strip()
            
            # Get last commit info
            result = subprocess.run(
                ['git', 'log', '-1', '--pretty=format:%H|%an|%ae|%ad|%s'],
                cwd=str(directory),
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                parts = result.stdout.strip().split('|')
                if len(parts) >= 5:
                    info['last_commit_hash'] = parts[0]
                    info['last_commit_author'] = parts[1]
                    info['last_commit_email'] = parts[2]
                    info['last_commit_date'] = parts[3]
                    info['last_commit_message'] = parts[4]
            
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as e:
            print(f"Git info error: {e}")
        
        return info
    
    def get_file_blame_info(self, directory: Path, filepath: str) -> Dict[str, any]:
        """Get blame info for a specific file"""
        if not self.is_git_repository(directory):
            return {}
        
        try:
            result = subprocess.run(
                ['git', 'log', '-1', '--pretty=format:%an|%ae|%ad|%s', '--', filepath],
                cwd=str(directory),
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode != 0:
                return {}
            
            if not result.stdout.strip():
                return {}
            
            parts = result.stdout.strip().split('|')
            if len(parts) >= 4:
                return {
                    'last_author': parts[0],
                    'last_author_email': parts[1],
                    'last_modified': parts[2],
                    'last_commit_message': parts[3]
                }
            
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as e:
            print(f"Git blame error: {e}")
        
        return {}
    
    def get_commits_affecting_files(self, directory: Path, files: List[str], limit: int = 10) -> List[Dict[str, str]]:
        """Get recent commits that affected the given files"""
        if not self.is_git_repository(directory) or not files:
            return []
        
        try:
            cmd = ['git', 'log', f'-{limit}', '--pretty=format:%H|%an|%ae|%ad|%s', '--'] + files
            
            result = subprocess.run(
                cmd,
                cwd=str(directory),
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                return []
            
            commits = []
            for line in result.stdout.strip().split('\n'):
                if not line:
                    continue
                
                parts = line.split('|')
                if len(parts) >= 5:
                    commits.append({
                        'hash': parts[0],
                        'author': parts[1],
                        'email': parts[2],
                        'date': parts[3],
                        'message': parts[4]
                    })
            
            return commits
            
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as e:
            print(f"Git log error: {e}")
            return []
    
    def filter_files_by_git_status(self, files: List[Dict[str, any]], 
                                 directory: Path, filter_type: str) -> List[Dict[str, any]]:
        """Filter files based on git status"""
        if not self.is_git_repository(directory):
            return files
        
        git_status = self.get_git_status(directory)
        
        if filter_type == 'all':
            return files
        elif filter_type == 'modified':
            target_files = set(git_status.get('modified', []) + git_status.get('staged', []))
        elif filter_type == 'untracked':
            target_files = set(git_status.get('untracked', []))
        elif filter_type == 'added':
            target_files = set(git_status.get('added', []))
        elif filter_type == 'changed':
            # All changed files (modified + added + untracked)
            target_files = set()
            for status_type in ['modified', 'added', 'untracked', 'staged']:
                target_files.update(git_status.get(status_type, []))
        elif filter_type.startswith('since_'):
            # since_hours_24, since_commit_HEAD~1, etc.
            if 'hours' in filter_type:
                hours = int(filter_type.split('_')[-1])
                target_files = set(self.get_changed_files_by_time(directory, hours))
            else:
                since = filter_type.replace('since_commit_', '')
                target_files = set(self.get_changed_files_since(directory, since))
        else:
            return files
        
        # Filter files
        filtered_files = []
        for file_info in files:
            if file_info['relative_path'] in target_files:
                filtered_files.append(file_info)
        
        return filtered_files
    
    def get_git_filters(self) -> List[Tuple[str, str]]:
        """Get available git-based filters"""
        return [
            ('all', 'All Files'),
            ('changed', 'All Changed Files'),
            ('modified', 'Modified Files'),
            ('added', 'Added Files'),
            ('untracked', 'Untracked Files'),
            ('since_hours_1', 'Changed in Last Hour'),
            ('since_hours_24', 'Changed in Last 24 Hours'),
            ('since_hours_168', 'Changed in Last Week'),
            ('since_commit_HEAD~1', 'Changed Since Last Commit'),
            ('since_commit_HEAD~5', 'Changed Since 5 Commits Ago')
        ]